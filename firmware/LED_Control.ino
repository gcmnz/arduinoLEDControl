long value = 0;  // Значение яркости для пина (0-255)
bool status = false;
uint32_t PIN = 6;  // D6 PIN

void setup() {
  pinMode(PIN, OUTPUT);
  analogWrite(PIN, 0);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { // Проверяем, есть ли входные данные
    uint32_t command = Serial.read(); // Читаем входные данные до символа новой строки

    if (command == 'd') {
      analogWrite(PIN, 0);
      status = false;
    }

    else if (command == 'e') {
      analogWrite(PIN, value);
      status = true;
    }

    else if (0 <= command <= 99) {
      value = map(command, 0, 99, 0, 255);

      if (status) {
        analogWrite(PIN, value);
      }
    }
  }
}