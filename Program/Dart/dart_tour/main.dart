void main() {
  var name = "ben";
  // name = 1;
  // name = bool;
  // name = true;
  // name = false;
  name = "hi";

  String name2 = "ben";

  // dynamic type
  var dynamic;
  // dynamic dynamic;
  dynamic = "ben";
  dynamic = 12;
  dynamic = true;

  if (dynamic is String) {
    // dynamic.
  } else if (dynamic is int) {
    // dynamic.
  }

  // null safety
  // isEmpty(null);
  String ben = "ben";
  // ben = null;
  String? ben2 = "ben";
  ben2 = null;
  // ben2.length;

  if (ben2 != null) {
    ben2.isNotEmpty;
  }
  // short cut, =
  ben2?.isNotEmpty;
}

// Without null safety:
bool isEmpty(String string) => string.length == 0;
