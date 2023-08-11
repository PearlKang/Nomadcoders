import 'package:go_router/go_router.dart';
import 'package:tiktok_clone/features/authentication/sign_up_screen.dart';

final router = GoRouter(
  routes: [
    GoRoute(
      path: "/",
      builder: (context, state) => const SignUpScreen(),
    ),
  ],
);
