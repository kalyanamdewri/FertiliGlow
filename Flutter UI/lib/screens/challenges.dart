import 'package:flutter/material.dart';

class ChallengesScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Challenges'),
      ),
      body: Center(
        child: Text(
          'Here you can see and complete challenges!',
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
