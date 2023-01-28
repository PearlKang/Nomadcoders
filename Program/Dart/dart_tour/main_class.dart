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

// positional - 데이터가 많아 지면 위치가 헷갈림. position이 너무 많아지면 뭐가 뭔지 몰라서 별로임.
class Player2 {
  final String name;
  int xp;
  String team;
  int age;

  Player2(this.name, this.xp, this.team, this.age);

  void sayHello() {
    print("hi my name is $name");
  }
}

class Player3 {
  final String name;
  int xp, age;
  String team;

  // Named Constructor parameter
  Player3({
    required this.name,
    required this.xp,
    required this.team,
    required this.age,
  });

  // syntax sugar
  // named parameter, named syntax - default not required
  Player3.createBluePlayer({
    required String name,
    required int age,
  })  : this.age = age,
        this.name = name,
        this.team = "blue",
        this.xp = 0;

  // positional parameter, positional syntax - default required
  Player3.createRedPlayer(String name, int age)
      : this.age = age,
        this.name = name,
        this.team = "red",
        this.xp = 0;

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

  // positional parameter
  var player3 = Player2("nico2", 1500, "red", 12);
  player3.sayHello();
  var player4 = Player2("lynn2", 2500, "blue", 12);
  player4.sayHello();

  // named parameter
  var player5 = Player3(
    name: "nico3",
    xp: 1200,
    team: "blue",
    age: 21,
  );
  player5.sayHello();
  var player6 = Player3(
    name: "lynn2",
    xp: 2500,
    team: "blue",
    age: 12,
  );
  player6.sayHello();

  // named parameter
  var bluePlayer = Player3.createBluePlayer(
    name: "nico",
    age: 21,
  );

  // positional parameter
  var redPlayer = Player3.createRedPlayer("nico", 21);
}
