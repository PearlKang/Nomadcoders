// enum - 실수를 줄여준다.
enum Team { red, blue }

enum XPLevel { beginner, medium, pro }

class Player {
  String name;
  XPLevel xp;
  Team team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
  });

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var nico = Player(
    name: "nico",
    xp: XPLevel.medium,
    team: Team.red,
  );
  nico.name = "las";
  nico.xp = XPLevel.pro;
  nico.team = Team.blue;

  // cascade operator, cascade notation
  var nico1 = Player(name: "nico", xp: XPLevel.medium, team: Team.red)
    ..name = "las"
    ..xp = XPLevel.beginner
    ..team = Team.blue;

  var nico2 = Player(name: "nico", xp: XPLevel.medium, team: Team.red);
  var potato = nico2
    ..name = "las"
    ..xp = XPLevel.pro
    ..team = Team.blue
    ..sayHello();
}
