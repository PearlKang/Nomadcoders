import 'package:flutter/material.dart';

// position
class Player1 {
  String name;

  Player1(this.name);
}

// named parameter
class Player2 {
  String name;

  Player2({required this.name});
}

class Player3 {
  String? name;

  Player3();
}

void main() {
  var ben1 = Player1("ben");
  var ben2 = Player2(name: "ben");
  var ben3 = Player3();

  runApp(App());
}

// Root Widget
class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Material = Google / Cupertino = ios // 테마 선택이라고 생각하면 됨.
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          centerTitle: false,
          elevation: 10,
          title: Text("Hello flutter!"),
        ),
        body: Center(
          child: Text("Hello World!"),
        ),
      ),
    );
  }
}
