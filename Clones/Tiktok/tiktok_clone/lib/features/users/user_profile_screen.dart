import 'package:flutter/material.dart';

class UserProfileScreen extends StatefulWidget {
  const UserProfileScreen({super.key});

  @override
  State<UserProfileScreen> createState() => _UserProfileScreenState();
}

class _UserProfileScreenState extends State<UserProfileScreen> {
  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: [
        SliverAppBar(
          backgroundColor: Colors.teal,
          elevation: 1,
          title: const Text("1 hello!"),
          collapsedHeight: 80,
          expandedHeight: 200,
          flexibleSpace: FlexibleSpaceBar(
            background: Image.asset(
              "assets/images/iu.jpg",
              fit: BoxFit.cover,
            ),
            title: const Text("2 hello!"),
          ),
        ),
      ],
    );
  }
}
