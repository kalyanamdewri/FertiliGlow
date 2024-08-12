import 'package:flutter/material.dart';

class LeaderboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Leaderboard'),
      ),
      body: Center(
        child: Text(
          'Check out the top performers here!',
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
