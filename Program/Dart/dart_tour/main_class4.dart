// inheritance - 상속
class Human {
  final String name;

  // Human(this.name);
  Human({required this.name});

  void sayHello() {
    print("Hi my name is $name");
  }
}

enum Team { blue, red }

class Player extends Human {
  final Team team;

  // super - extends
  Player({
    required this.team,
    required String name,
  }) : super(name: name); // : super(name)

  @override
  void sayHello() {
    super.sayHello();
    print("and i play for ${team}");
  }
}

void main() {
  var player = Player(team: Team.red, name: "ben");
}
