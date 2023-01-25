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

void main() {
  // var player = new Player();
  var player = Player();

  print(player.name);

  // final 때문에 아래 안댐.
  // player.name = "adsfasdfsad";
  // print(player.name);

  player.sayHello();
  player.sayHello2();
}
