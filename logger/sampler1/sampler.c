#include <wiringPi.h>
#include <stdio.h>

int main (void)
{
  int pin_switch = 9; // GPIO1 original layout - GPIO3 on REV 2


  double del = 0.4167;
  //int del = 250;

  if (wiringPiSetup() == -1) return 1;

  pinMode(pin_switch, INPUT);

  for (;;){
    if (digitalRead (pin_switch) == 0)
        printf("0");
    else
        printf("1");

//    if (digitalRead (pin_switch) == 1)
//        printf("1");
  delay(del);
  }

  return 0 ;
}
