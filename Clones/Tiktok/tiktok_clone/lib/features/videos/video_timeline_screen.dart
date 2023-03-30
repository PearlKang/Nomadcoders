import 'package:flutter/material.dart';

class VideoTimelineScreen extends StatefulWidget {
  const VideoTimelineScreen({super.key});

  @override
  State<VideoTimelineScreen> createState() => _VideoTimelineScreenState();
}

class _VideoTimelineScreenState extends State<VideoTimelineScreen> {
  @override
  Widget build(BuildContext context) {
    return PageView(
      pageSnapping: true,
      scrollDirection: Axis.vertical,
      children: [
        Container(
          color: Colors.blue,
        ),
        Container(
          color: Colors.teal,
        ),
        Container(
          color: Colors.yellow,
        ),
        Container(
          color: Colors.pink,
        ),
      ],
    );
  }
}
