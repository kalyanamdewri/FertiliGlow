import 'package:flutter/material.dart';

class LogDataScreen extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Log Today\'s Data'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: <Widget>[
              TextFormField(
                decoration: InputDecoration(labelText: 'Mood'),
                validator: (value) {
                  if (value.isEmpty) {
                    return 'Please enter your mood';
                  }
                  return null;
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Temperature (°C)'),
                keyboardType: TextInputType.number,
                validator: (value) {
                  if (value.isEmpty) {
                    return 'Please enter your temperature';
                  }
                  return null;
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Diet'),
                maxLines: 3,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Exercise'),
                maxLines: 3,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Sleep Hours'),
                keyboardType: TextInputType.number,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Notes'),
                maxLines: 5,
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState.validate()) {
                    // Save the log data
                    ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Data logged successfully')));
                  }
                },
                child: Text('Submit'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
