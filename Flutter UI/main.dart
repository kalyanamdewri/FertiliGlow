import 'package:flutter/material.dart';
import 'screens/dashboard.dart';
import 'screens/log_data.dart';
import 'screens/challenges.dart';
import 'screens/leaderboard.dart';
import 'screens/profile.dart';

void main() {
  runApp(FertiliGlowApp());
}

class FertiliGlowApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FertiliGlow',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: DashboardScreen(),
      routes: {
        '/log_data': (context) => LogDataScreen(),
        '/challenges': (context) => ChallengesScreen(),
        '/leaderboard': (context) => LeaderboardScreen(),
        '/profile': (context) => ProfileScreen(),
      },
    );
  }
}
