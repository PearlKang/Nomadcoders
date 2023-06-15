import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SettingScreen extends StatelessWidget {
  const SettingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Settings"),
      ),
      body: Column(
        children: const [
          CupertinoActivityIndicator(
            radius: 40,
            animating: false,
          ),
          CircularProgressIndicator(),
          CircularProgressIndicator.adaptive(),
        ],
      ),
    );
  }
}
