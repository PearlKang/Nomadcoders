import 'package:flutter/material.dart';
import 'package:toonflix/models/webtoon_episode_model.dart';
import 'package:url_launcher/url_launcher.dart';

class Episode extends StatelessWidget {
  const Episode({
    super.key,
    required this.episode,
  });

  final WebtoonEpisodeModel episode;

  onButtonTap() async {
    // await launchUrlString("https://google.com");
    final url = Uri.parse("https://google.com");
    await launchUrl(url);
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(
        bottom: 10,
      ),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: Colors.white,
        border: Border.all(
          color: Colors.green.shade400,
          width: 1.5,
        ),
        boxShadow: [
          BoxShadow(
            blurRadius: 3,
            offset: const Offset(5, 5),
            color: Colors.black.withOpacity(0.5),
          ),
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 10,
          horizontal: 20,
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              episode.title,
              style: TextStyle(
                color: Colors.green.shade400,
                fontSize: 16,
              ),
            ),
            Icon(
              Icons.chevron_right_rounded,
              color: Colors.green.shade400,
            ),
          ],
        ),
      ),
    );
  }
}
