import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:tiktok_clone/constants/gaps.dart';
import 'package:tiktok_clone/constants/sizes.dart';

class ActivityScreen extends StatelessWidget {
  const ActivityScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("All activity"),
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(
          horizontal: 0,
        ),
        children: [
          Gaps.v14,
          Text(
            "New",
            style: TextStyle(
              fontSize: Sizes.size14,
              color: Colors.grey.shade500,
            ),
          ),
          Gaps.v14,
          Dismissible(
            key: const Key("X"),
            background: Container(
              color: Colors.green,
              child: const Padding(
                padding: EdgeInsets.only(
                  left: Sizes.size10,
                ),
                child: FaIcon(FontAwesomeIcons.checkDouble),
              ),
            ),
            child: ListTile(
              leading: Container(
                width: Sizes.size52,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.white,
                  border: Border.all(
                    color: Colors.grey.shade400,
                    width: Sizes.size1,
                  ),
                ),
                child: const Center(
                  child: FaIcon(
                    FontAwesomeIcons.bell,
                    color: Colors.black,
                  ),
                ),
              ),
              title: RichText(
                text: TextSpan(
                  text: "Account updates:",
                  style: const TextStyle(
                    fontWeight: FontWeight.w600,
                    color: Colors.black,
                    fontSize: Sizes.size16,
                  ),
                  children: [
                    const TextSpan(
                      text: " Upload longer videos",
                      style: TextStyle(
                        fontWeight: FontWeight.normal,
                      ),
                    ),
                    TextSpan(
                      text: " 1 h",
                      style: TextStyle(
                        fontWeight: FontWeight.normal,
                        color: Colors.grey.shade500,
                      ),
                    ),
                  ],
                ),
              ),
              trailing: const FaIcon(
                FontAwesomeIcons.chevronRight,
                size: Sizes.size16,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
