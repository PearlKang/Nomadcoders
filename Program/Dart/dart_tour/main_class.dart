class Player {
  final String name = "ben";
  int xp = 1500;

  void sayHello() {
    print("Hi my name is $name");
  }

  void sayHello2() {
    var name = "123";
    print("1 Hi my name is ${this.name}");
    print("2 Hi my name is $name");
  }
}

class Player1 {
  late final String name;
  late int xp;

  Player1(String name, int xp) {
    this.name = name;
    this.xp = xp;
  }

  void sayHello() {
    print("hi my name is $name");
  }
}

class Player2 {
  final String name;
  int xp;

  Player2(this.name, this.xp);

  void sayHello() {
    print("hi my name is $name");
  }
}

void main() {
  // var player = new Player();
  var player = Player();

  print(player.name);

  // final 때문에 아래 안댐.
  // player.name = "adsfasdfsad";
  // print(player.name);

  player.sayHello();
  player.sayHello2();

  // Constructors
  var player1 = Player1("nico1", 1500);
  player1.sayHello();
  var player2 = Player1("lynn1", 2500);
  player2.sayHello();
  var player3 = Player2("nico2", 1500);
  player3.sayHello();
  var player4 = Player2("lynn2", 2500);
  player4.sayHello();
}
