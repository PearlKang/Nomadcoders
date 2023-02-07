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
        body: Text("Hello World!"),
      ),
    );
  }
}
