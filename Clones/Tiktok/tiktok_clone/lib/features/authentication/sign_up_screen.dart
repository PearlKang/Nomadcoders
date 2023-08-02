import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:tiktok_clone/constants/gaps.dart';
import 'package:tiktok_clone/constants/sizes.dart';
import 'package:tiktok_clone/features/authentication/login_screen.dart';
import 'package:tiktok_clone/features/authentication/username_screen.dart';
import 'package:tiktok_clone/features/authentication/widgets/auth_button.dart';
import 'package:tiktok_clone/generated/l10n.dart';
import 'package:tiktok_clone/utils.dart';

class SignUpScreen extends StatelessWidget {
  const SignUpScreen({super.key});

  void _onLoginTap(BuildContext context) async {
    await Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => const LoginScreen(),
      ),
    );
    print("user came back");
  }

  void _onEmailTap(BuildContext context) {
    Navigator.of(context).push(
      PageRouteBuilder(
        transitionDuration: const Duration(
          seconds: 1,
        ),
        reverseTransitionDuration: const Duration(
          seconds: 1,
        ),
        pageBuilder: (context, animation, secondaryAnimation) =>
            const UsernameScreen(),
        transitionsBuilder: (context, animation, secondaryAnimation, child) =>
            ScaleTransition(
          scale: animation,
          alignment: Alignment.bottomRight,
          child: FadeTransition(
            opacity: animation,
            child: child,
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return OrientationBuilder(
      builder: (context, orientation) {
        return Scaffold(
          body: SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(
                horizontal: Sizes.size40,
              ),
              child: Column(
                children: [
                  Gaps.v80,
                  Text(
                    S.of(context).signUpTitle(
                          "TikTok",
                          DateTime.now(),
                        ),
                    style: const TextStyle(
                      fontSize: Sizes.size24,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  Gaps.v20,
                  Opacity(
                    opacity: 0.7,
                    child: Text(
                      S.of(context).signUpSubtitle(1),
                      style: const TextStyle(
                        fontSize: Sizes.size16,
                      ),
                      textAlign: TextAlign.center,
                    ),
                  ),
                  Gaps.v40,
                  if (orientation == Orientation.portrait) ...[
                    GestureDetector(
                      onTap: () => _onEmailTap(context),
                      child: AuthButton(
                        icon: const FaIcon(
                          FontAwesomeIcons.user,
                        ),
                        text: S.of(context).emailPasswordButton,
                      ),
                    ),
                    Gaps.v16,
                    AuthButton(
                      icon: const FaIcon(
                        FontAwesomeIcons.apple,
                      ),
                      text: S.of(context).appleButton,
                    ),
                  ],
                  if (orientation == Orientation.landscape)
                    Row(
                      children: [
                        Expanded(
                          child: GestureDetector(
                            onTap: () => _onEmailTap(context),
                            child: AuthButton(
                              icon: const FaIcon(
                                FontAwesomeIcons.user,
                              ),
                              text: S.of(context).emailPasswordButton,
                            ),
                          ),
                        ),
                        Gaps.h16,
                        Expanded(
                          child: AuthButton(
                            icon: const FaIcon(
                              FontAwesomeIcons.apple,
                            ),
                            text: S.of(context).appleButton,
                          ),
                        ),
                      ],
                    ),
                ],
              ),
            ),
          ),
          bottomNavigationBar: Container(
            color: isDarkMode(context)
                ? Theme.of(context).appBarTheme.backgroundColor
                : Colors.grey.shade50,
            child: Padding(
              padding: const EdgeInsets.only(
                top: Sizes.size32,
                bottom: Sizes.size64,
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    S.of(context).alreadyHaveAnAccount,
                    style: const TextStyle(
                      fontSize: Sizes.size16,
                    ),
                  ),
                  Gaps.h5,
                  GestureDetector(
                    onTap: () => _onLoginTap(context),
                    child: Text(
                      S.of(context).logIn("female"),
                      style: TextStyle(
                        fontWeight: FontWeight.w600,
                        color: Theme.of(context).primaryColor,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
