import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:tiktok_clone/constants/gaps.dart';
import 'package:tiktok_clone/constants/sizes.dart';

class VideoButton extends StatelessWidget {
  final IconData _icon;
  final String _text;

  const VideoButton({
    super.key,
    required icon,
    required text,
  })  : _icon = icon,
        _text = text;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        FaIcon(
          _icon,
          color: Colors.white,
          size: Sizes.size40,
        ),
        Gaps.v5,
        Text(
          _text,
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
      ],
    );
  }
}
