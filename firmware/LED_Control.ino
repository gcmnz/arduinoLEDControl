void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW); // Выключаем светодиод при инициализации
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { // Проверяем, есть ли входные данные
    int command = Serial.read(); // Читаем входные данные до символа новой строки
  
    if (0 <= command <= 99) {
      // analogWrite
    }

    else if (command == 100) {
      digitalWrite(LED_BUILTIN, LOW); // Выключаем светодиод
    }

    else if (command == 101) {
      digitalWrite(LED_BUILTIN, HIGH); // Включаем светодиод
    }
  }
}
