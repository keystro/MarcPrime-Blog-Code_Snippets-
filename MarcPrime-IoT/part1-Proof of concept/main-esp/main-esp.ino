#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

const char * ssid = "Marc";
const char * password = "8c6c54bee1661a6e";

//const char * ssid = "Nokia 5.1";
//const char * password = "alpha2019";

void setup(void){

  Serial.begin(115200);
 

  Serial.println("Establishing Connecting . . . .  ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  while (WiFi.status() !=WL_CONNECTED){

    delay(500);
    Serial.print("*");
  }

  Serial.println("WiFi Connection Established . . . . ");
  Serial.print(WiFi.localIP());

  
}
void loop(){

  if (WiFi.status() == WL_CONNECTED) {

    //Json Data
    StaticJsonDocument<100> doc;
    JsonObject root = doc.to<JsonObject>();

    root ["ipaddr"] = WiFi.localIP(); 
    root ["name"] = "MarcPrime Main Termx";
   
    char JSONmessageBuffer[100];
    serializeJsonPretty(root, JSONmessageBuffer);
    Serial.println(JSONmessageBuffer);

    HTTPClient http;


    http.begin("http://192.168.1.104:5000/index");
    http.addHeader("Content-Type", "application/json");
    int httpCode2 = http.POST(JSONmessageBuffer);
    String payload2 = http.getString();
    Serial.println("Http response code for POST REQUEST 029OMEGA: ");
    Serial.println(payload2);

    http.end();
  }
  delay(100000);
 
}
