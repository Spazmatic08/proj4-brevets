"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

from collections import namedtuple

# Lookup table for brevet distance to speeds. Since there's
# No direct logical rule for calculating them, it's simpler
# and easier to modify by keeping them in one discrete place.

# Speeds are dictated by where precisely the control in question
# is placed on the entire brevet. They are divided by thresholds,
# which must be *met* to progress to the next one, so long
# as the brevet length is shorter than the actual position of the
# control. The controls are cumulative - the first 200 km use the
# 0-200 range, the next 200 the 200-400 range, and so on.

# With the exceptions of 200 and 400 km brevets, the times of
# the final control (the race's end) is treated as though it were
# only as long as the brevet's classification. So even if the final
# control of a 300 km brevet were at 304 km, both of the times are
# calculated as though it were positioned at 300 km.

SpeedLimit = namedtuple('SpeedLimit', ['threshold', 'speedtype'])

limits = {SpeedLimit(threshold=0, speedtype='slow'):15.0,
          SpeedLimit(threshold=0, speedtype='fast'):34.0,
          SpeedLimit(threshold=200, speedtype='slow'):15.0,
          SpeedLimit(threshold=200, speedtype='fast'):32.0,
          SpeedLimit(threshold=400, speedtype='slow'):15.0,
          SpeedLimit(threshold=400, speedtype='fast'):30.0,
          SpeedLimit(threshold=600, speedtype='slow'):11.428,
          SpeedLimit(threshold=600, speedtype='fast'):28.0,
          SpeedLimit(threshold=1000, speedtype='slow'):13.333,
          SpeedLimit(threshold=1000, speedtype='fast'):26.0}

# EXCEPTIONS:
# Because reasons, the brevets include a number of rules that supercede
# the patterns described above, They are as follows:
#   - The closing time of the starting checkpoint for a brevet is
#       always one hour after it opens.
#   - The overall time limit for a 200 km brevet is always 13.5
#       hours, regardless of the actual position of the final
#       control.
#   - The overall time limit for a 400 km brevet is always 27 hours,
#       regardless of the actual position of the final control.

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    start = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return brevet_start_time  # See Exceptions

    return calc_time( control_dist_km,
                      'fast',
                      brevet_dist_km,
                      start )
    

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    start = arrow.get(brevet_start_time)

    if control_dist_km == 0:
        return start.replace(hours=+1).isoformat()     # See Exceptions
    elif control_dist_km >= 200 and brevet_dist_km == 200:
        return start.replace(hours=+13.5).isoformat()  # See Exceptions
    elif control_dist_km >= 400 and brevet_dist_km == 400:
        return start.replace(hours=+27).isoformat()    # See Exceptions

    return calc_time( control_dist_km,
                      'slow',
                      brevet_dist_km,
                      start )

def calc_time( control_position, speedtype, brevet_max, start_time ):
    """
    Takes the characteristics of the controle position and the type of speed
    limit sought, as well as the brevet's maximum, and returns the ISO 8601
    format string for the time.
    """
    # The dictionary keys are all named tuples - SpeedLimits. At their
    # 0 index, they contain the valid thresholds listed in the limits.
    # We want the whole list of thresholds so we can calculate the totals,
    # so we just gather all of them that are less than or equal to the
    # control's position. If the control is past the brevet's end, we use
    # the brevet as the maximum to avoid getting too high a speed category.
    if (control_position < brevet_max):
        thresholds = sorted(set(SL[0] for SL in limits.keys()
                         if SL[0] <= control_position))
    else:
        thresholds = sorted(set(SL[0] for SL in limits.keys()
                         if SL[0] < brevet_max))

    print("valid thresholds: {}".format(thresholds))

    max_threshold = thresholds.pop()

    # We now have the highest distance category of the brevet, so we need
    # to sum the maximum from all categories before it. 
    result = 0.0
    temp = max_threshold
    while not not thresholds:
        threshold = thresholds.pop()
        distance = temp - threshold
        print("Distance {} for threshold {}".format(distance, threshold))
        speed = limits[SpeedLimit(threshold, speedtype)]
        print("Speed tied to that threshold: {}".format(speed))
        result += distance / speed
        print("Total resulting offset: {}".format(result))
        temp = threshold

    # Now we just need whatever's left over in the highest distance category.
    # Note that if the distance is greater than the brevet length, we have to
    # cut it down to the length of the brevet itself.
    if control_position >= brevet_max:
        control_position = brevet_max
    remaining_distance = control_position - max_threshold
    print("Distance {} for threshold {}".format(remaining_distance, max_threshold))
    remaining_speed = limits[SpeedLimit(max_threshold, speedtype)]
    print("Speed tied to that threshold {}".format(remaining_speed))

    result += remaining_distance / remaining_speed
    print("Total resulting offset: {}".format(result))

    # Round it off to avoid numbers too generous
    result_hours, result_mins = round_offset(result)
    print("Rounded result: {} hours, {} minutes".format(result_hours, result_mins))

    return start_time.replace(
        hours=+result_hours,
        minutes=+result_mins).isoformat()

def round_offset( offset ):
    """
    Rounds a raw hours offset into hours and minutes offsets based on the
    RUSA specifications.
    """
    # Hours is easy. Just floor the offset.
    offset_hours = math.floor(offset)

    # Minutes, we need to take the decimal portion of offset and multiply
    # it by 60, then round it too.
    offset_mins = round((offset % 1) * 60.0, 0)

    return offset_hours, offset_mins
