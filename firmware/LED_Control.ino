void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW); // Выключаем светодиод при инициализации
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { // Проверяем, есть ли входные данные
    char command = Serial.read(); // Читаем входные данные до символа новой строки

    if (command == 'd') {
      digitalWrite(LED_BUILTIN, LOW); // Выключаем светодиод
    }

    else if (command == 'e') {
      digitalWrite(LED_BUILTIN, HIGH); // Включаем светодиод
    }
  }
}