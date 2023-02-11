import 'package:flutter/material.dart';

void main() {
  runApp(App());
}

// Root Widget
class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Material = Google / Cupertino = ios // 테마 선택이라고 생각하면 됨.
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Colors.black,
          body: Column(
            children: [
              Row(
                children: [
                  Column(
                    children: [
                      Text(
                        "Hey, Selena",
                        style: TextStyle(
                          color: Colors.white,
                        ),
                      ),
                      Text(
                        "Welcome back",
                        style: TextStyle(
                          color: Colors.white,
                        ),
                      ),
                    ],
                  )
                ],
              )
            ],
          )),
    );
  }
}
