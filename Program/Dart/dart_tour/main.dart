void main() {
  // var name = "ben";
  // name = 1;
  // name = bool;
  // name = true;
  // name = false;
  // name = "hi";

  // String name = "ben";

  // dynamic type
  // var dynamic;
  // dynamic dynamic;
  // dynamic = "ben";
  // dynamic = 12;
  // dynamic = true;

  // if (dynamic is String) {
  // dynamic.
  // } else if (dynamic is int) {
  // dynamic.
  // }

  // null safety
  // isEmpty(null);
  // String ben = "ben";
  // ben = null;
  // String? ben = "ben";
  // ben = null;
  // ben.length;

  // if (ben != null) {
  //   ben.isNotEmpty;
  // }
  // short cut, =
  // ben?.isNotEmpty;

  // final type
  // var name = "ben";
  // String name = "ben";
  // String x = "ben";
  // name = "last";
  // final String name = "ben";
  // final name = "ben";

  // late type
  // late final String name;
  // do something, go to api
  // print(name);
  // name = "ben";
  // name = "12";

  // const type
  // const name = "ben";
  // name = "12";
  // const API = "121212";
  // const API = fetchApi();
  // final API = fetchApi();

  // Recap
  // int i = 12;
  // var name = "la";
  // i = 12211212;
  // name = "lalalal";

  // once = final
  // final name = "ben";
  // name = "wefwefwef";

  // dynamic type
  // dynamic name;
  // name = "1212";
  // name = 12;
  // name = true;
  // if(name is String) {
  //   name.
  // }

  // const type - 컴파일 할때 값을 알고 있는 변수를 만들 때, 앱스토어에 앱을 올리기 전에
  // const api_key = "121212121212";
  // api_key = 123123123;

  // final type - 런타임 중에 만들어 질 수 있는,
  // final String username;

  // null safety
  // String name = "ben";
  // name = null;
  // String? name = "ben";
  // name = null;
  // name.isEmpty;
  // if (name != null) {
  //   name.isEmpty;
  // }
  // name?.isEmpty;

  // late type - late + final, var, String ...
  // late final String name;
  // print(name);
  // name = "12";
  // print(name);

  // basic data types
  // String name = "ben";
  // name = 'change';
  // name.
  // bool alive = true;
  // int age = 12;
  // age.
  // double money = 69.99;
  // num x = 12;
  // x = 1.1;

  // lists
  // var numbers2 = [1, 2, 3, 4];
  // List<int> numbers = [1, 2, 3, 4];
  // numbers.add("1234124");
  // numbers.add(1);
  // var giveMeFive = true;
  // var numbers = [
  //   1,
  //   2,
  //   3,
  //   4,
  //   if (giveMeFive) 5,
  // ];
  // if (giveMeFive) {
  //   numbers.add(5);
  // }
  // print(numbers);

  // String Interpolation
  // var name = "ben";
  // var age = 10;
  // var greeting =
  //     "Hello everyone, my name is $name, and I\'m ${age + 2}, nice to meet you!";

  // print(greeting);

  // Collection For
  // var oldFriends = ["nico", "lynn"];
  // var newFriends = [
  //   "lewis",
  //   "ralph",
  //   "darren",
  //   for (var friend in oldFriends) "💖 $friend",
  // ];

  // print(newFriends);

  // Map: Key, Value
  // var player = {
  //   "name": "ben",
  //   "xp": 19.99,
  //   "superpower": false,
  // };
  // Map<int, bool> player2 = {
  //   1: true,
  //   2: false,
  //   3: true,
  //   // 4:"12",
  // };
  // Map<List<int>, bool> player3 = {
  //   [1, 2, 3]: true,
  // };
  // List<Map<String, Object>> players = [
  //   {
  //     "name": "ben",
  //     "xp": 199993.999,
  //   },
  //   {
  //     "name": "ben",
  //     "xp": 199993.999,
  //   },
  // ];

  // Set - unique
  // var numbers = {1, 2, 3, 4};
  // Set<int> numbers2 = {1, 2, 3, 4};
  // numbers.add(1);
  // numbers.add(1);
  // numbers.add(1);
  // numbers.add(1);
  // print(numbers);

  // Function
  // sayHello("ben1");
  // print(sayHello2("ben2"));
  // print(sayHello3("ben3"));

  // Named Parameters
  // print(sayHello4("ben", 36, "South Korea"));

  // named argument
  // print(sayHello5(
  //   name: "ben",
  //   age: 36,
  //   country: "S.K",
  // ));

  // print(sayHello6(
  //   name: "ben",
  //   age: 36,
  //   country: "S.K",
  // ));

  // Optonal Positional Parameters
  // sayHello7("ben", 12);

  // var results = sayHello7("Ben", 12);
  // print(results);
  // results = sayHello7("Ben", 12, "wefwefwe");
  // print(results);

  // QQ Operator (question) - ??, question question, null aware operator
  print(capitalizeName("ben"));
  print(capitalizeName2(null));

  String? name;
  name ??= "ben";
  print(name);
  name = null;
  print(name);
  name ??= "another";
  print(name);
}

// Without null safety:
bool isEmpty(String string) => string.length == 0;

void sayHello(String name) {
  print("Hello $name nice to meet you!");
}

String sayHello2(String name) {
  return "Hello $name nice to meet you!";
}

// fat arrow syntax
String sayHello3(String name) => "Hello $name nice to meet you!";

num plus(num a, num b) => a + b;

// positional parameter
String sayHello4(String name, int age, String country) {
  return "Hello $name, you are $age, and you come from $country";
}

// named argument - null safety - default value
String sayHello5({
  String name = "anon",
  int age = 99,
  String country = "wakanda",
}) {
  return "Hello $name, you are $age, and you come from $country";
}

// named argument - null safety - required modifier
String sayHello6({
  required String name,
  required int age,
  required String country,
}) {
  return "Hello $name, you are $age, and you come from $country";
}

// Optional Position Parameters
String sayHello7(String name, int age, [String? country = "cuba"]) =>
    "Hello $name, you are $age years old from $country";

// QQ Operator
String capitalizeName(String name) => name.toUpperCase();

String capitalizeName2(String? name) {
  if (name != null) {
    return name.toUpperCase();
  }
  return "ANON";
}

// ternary operator - 3항연산자
String capitalizeName3(String? name) =>
    name != null ? name.toUpperCase() : "ANON";

// question question operator - 왼쪽이 null이면 오른쪽, 아니면 왼쪽
String capitalizeName4(String? name) => name?.toUpperCase() ?? "ANON";
