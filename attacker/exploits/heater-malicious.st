PROGRAM program0
  VAR
    max_temp AT %IW0 : INT := 98;
    max_pressure AT %IW1 : INT := 500;
    on_button AT %QX0.0 : BOOL := TRUE;
    level_sensor_low AT %IX100.0 : BOOL := FALSE;
    level_sensor_high AT %IX100.1 : BOOL := FALSE;
    thermometer AT %IW100 : INT;
    pressure_gauge AT %IW101 : INT;
    heater_on AT %QX100.0 : BOOL;
    water_on AT %QX100.1 : BOOL;
    drain_on AT %QX100.2 : BOOL;
  END_VAR
  VAR
    AND40_OUT : BOOL;
    AND15_OUT : BOOL;
    AND26_OUT : BOOL;
    LT22_OUT : BOOL;
    LT34_OUT : BOOL;
    AND33_OUT : BOOL;
    AND23_OUT : BOOL;
  END_VAR

  AND40_OUT := AND(NOT(level_sensor_high), on_button);
  water_on := AND40_OUT;
  AND15_OUT := AND(NOT(on_button), level_sensor_low);
  drain_on := AND15_OUT;
  AND26_OUT := AND(on_button, level_sensor_high);
  LT22_OUT := LT(thermometer, max_temp);
  LT34_OUT := LT(pressure_gauge, max_pressure);
  AND33_OUT := AND(LT22_OUT, LT34_OUT);
  AND23_OUT := AND(AND26_OUT, AND33_OUT);
  heater_on := AND23_OUT;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : program0;
  END_RESOURCE
END_CONFIGURATION
