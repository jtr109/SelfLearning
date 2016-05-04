#include <stdio.h>

struct time
{
    int hour;
    int minutes;
    int seconds;
};


struct time elapsed_time (struct time time1, struct time time2)
{
    struct time distanceOfTime;
    
    if (time2.seconds < time1.seconds) {
        time2.minutes -= 1;
        distanceOfTime.seconds = time2.seconds + 60 - time1.seconds;
    } else {
        distanceOfTime.seconds = time2.seconds - time1.seconds;
    }
    
    if (time2.minutes < time1.minutes) {
        time2.hour -= 1;
        distanceOfTime.minutes = time2.minutes + 60 - time1.minutes;
    } else {
        distanceOfTime.minutes = time2.minutes - time1.minutes;
    }
    
    if (time2.hour < time1.hour)
        distanceOfTime.hour = time2.hour + 24 - time1.hour;
    else
        distanceOfTime.hour = time2.hour - time1.hour;
        
    return distanceOfTime;
};


int main(void)
{
    struct time time1, time2, distanceOfTime;
    struct time elapsed_time (struct time time1, struct time time2);
    
    printf("time1 = ");
    scanf("%d:%d:%d", &time1.hour, &time1.minutes, &time1.seconds);
    printf("time2 = ");
    scanf("%d:%d:%d", &time2.hour, &time2.minutes, &time2.seconds);
    
    distanceOfTime = elapsed_time(time1, time2);
    
    printf("The distance of time1 and time2 is %d:%d:%d\n", distanceOfTime.hour, distanceOfTime.minutes, distanceOfTime.seconds);
    
    return 0;
}