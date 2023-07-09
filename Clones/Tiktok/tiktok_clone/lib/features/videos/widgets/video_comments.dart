import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:tiktok_clone/constants/breakpoints.dart';
import 'package:tiktok_clone/constants/gaps.dart';
import 'package:tiktok_clone/constants/sizes.dart';

class VideoComments extends StatefulWidget {
  const VideoComments({super.key});

  @override
  State<VideoComments> createState() => _VideoCommentsState();
}

class _VideoCommentsState extends State<VideoComments> {
  bool _isWriting = false;

  final ScrollController _scrollController = ScrollController();

  void _onClosedPressed() {
    Navigator.of(context).pop();
  }

  void _stopWriting() {
    FocusScope.of(context).unfocus();
    setState(() {
      _isWriting = false;
    });
  }

  void _onStartWriting() {
    setState(() {
      _isWriting = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Align(
      alignment: Alignment.bottomCenter,
      child: Container(
        constraints: const BoxConstraints(
          maxWidth: Breakpoints.sm,
        ),
        height: size.height * 0.75,
        clipBehavior: Clip.hardEdge,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(
            Sizes.size14,
          ),
        ),
        child: Scaffold(
          backgroundColor: Colors.grey.shade50,
          appBar: AppBar(
            automaticallyImplyLeading: false,
            title: const Text("22796 comments"),
            actions: [
              IconButton(
                onPressed: _onClosedPressed,
                icon: const FaIcon(
                  FontAwesomeIcons.xmark,
                ),
              ),
            ],
          ),
          body: GestureDetector(
            onTap: _stopWriting,
            child: Stack(
              children: [
                Scrollbar(
                  controller: _scrollController,
                  child: ListView.separated(
                    controller: _scrollController,
                    padding: const EdgeInsets.only(
                      top: Sizes.size10,
                      bottom: Sizes.size96 + Sizes.size20,
                      left: Sizes.size16,
                      right: Sizes.size16,
                    ),
                    separatorBuilder: (context, index) => Gaps.v20,
                    itemCount: 10,
                    itemBuilder: (context, index) => Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const CircleAvatar(
                          radius: 18,
                          child: Text("Ben"),
                        ),
                        Gaps.h10,
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                "Ben",
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: Sizes.size14,
                                  color: Colors.grey.shade500,
                                ),
                              ),
                              Gaps.v3,
                              const Text(
                                "That's not it l've seen the same thing but also in a cave",
                              ),
                            ],
                          ),
                        ),
                        Gaps.h10,
                        Column(
                          children: [
                            FaIcon(
                              FontAwesomeIcons.heart,
                              size: Sizes.size20,
                              color: Colors.grey.shade500,
                            ),
                            Gaps.v2,
                            Text(
                              "52.2K",
                              style: TextStyle(
                                color: Colors.grey.shade500,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
                Positioned(
                  bottom: 0,
                  width: size.width,
                  child: BottomAppBar(
                    color: Colors.white,
                    child: Padding(
                      padding: const EdgeInsets.symmetric(
                        horizontal: Sizes.size16,
                        vertical: Sizes.size10,
                      ),
                      child: Row(
                        children: [
                          CircleAvatar(
                            radius: 18,
                            backgroundColor: Colors.grey.shade500,
                            foregroundColor: Colors.white,
                            child: const Text("Ben"),
                          ),
                          Gaps.h10,
                          Expanded(
                            child: SizedBox(
                              height: Sizes.size44,
                              child: TextField(
                                onTap: _onStartWriting,
                                expands: true,
                                minLines: null,
                                maxLines: null,
                                textInputAction: TextInputAction.newline,
                                cursorColor: Theme.of(context).primaryColor,
                                decoration: InputDecoration(
                                  hintText: "Write a comment...",
                                  border: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(
                                      Sizes.size12,
                                    ),
                                    borderSide: BorderSide.none,
                                  ),
                                  filled: true,
                                  fillColor: Colors.grey.shade200,
                                  contentPadding: const EdgeInsets.symmetric(
                                    horizontal: Sizes.size10,
                                  ),
                                  suffixIcon: Padding(
                                    padding: const EdgeInsets.only(
                                      right: Sizes.size14,
                                    ),
                                    child: Row(
                                      mainAxisSize: MainAxisSize.min,
                                      children: [
                                        FaIcon(
                                          FontAwesomeIcons.at,
                                          color: Colors.grey.shade900,
                                        ),
                                        Gaps.h14,
                                        FaIcon(
                                          FontAwesomeIcons.gift,
                                          color: Colors.grey.shade900,
                                        ),
                                        Gaps.h14,
                                        FaIcon(
                                          FontAwesomeIcons.faceSmile,
                                          color: Colors.grey.shade900,
                                        ),
                                        if (_isWriting) Gaps.h14,
                                        if (_isWriting)
                                          GestureDetector(
                                            onTap: _stopWriting,
                                            child: FaIcon(
                                              FontAwesomeIcons.circleArrowUp,
                                              color: Theme.of(context)
                                                  .primaryColor,
                                            ),
                                          ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
