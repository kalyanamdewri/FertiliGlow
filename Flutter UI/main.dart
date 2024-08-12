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



class FertiliGlowApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FertiliGlow',
      theme: ThemeData(
        primaryColor: Colors.teal,
        accentColor: Colors.orange,
        buttonTheme: ButtonThemeData(buttonColor: Colors.teal),
        textTheme: TextTheme(
          headline1: TextStyle(fontSize: 36.0, fontWeight: FontWeight.bold),
          headline6: TextStyle(fontSize: 18.0, fontStyle: FontStyle.italic),
          bodyText2: TextStyle(fontSize: 14.0, fontFamily: 'Hind'),
        ),
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
