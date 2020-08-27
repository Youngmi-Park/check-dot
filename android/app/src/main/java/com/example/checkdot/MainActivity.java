package com.example.checkdot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.example.checkdot.AboutUs.AboutActivity;
import com.example.checkdot.Help.HelpActivity;
import com.example.checkdot.LearningBraille.LearningActivity;
import com.example.checkdot.ReportBoard.BoardActivity;
import com.example.checkdot.ReportForm.ReportformActivity;
import com.example.checkdot.TranslationCamera.CameraActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


       View translateBtn = findViewById(R.id.button1);
       View studyBtn = findViewById(R.id.button2);
       View sirenBtn = findViewById(R.id.button3);
       View boardBtn = findViewById(R.id.button4);
       View helpBtn = findViewById(R.id.button5);
       View aboutBtn = findViewById(R.id.button6);


       //한글로 번역하기
        translateBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), CameraActivity.class);
                startActivity(intent);
                //슬라이드 효과
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });

        //점자 공부하기
        studyBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), LearningActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });

        //신고하기
        sirenBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), ReportformActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });

        //신고 게시판
        boardBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), BoardActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });

        //도움말
        helpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), HelpActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });

        //about
        aboutBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), AboutActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
            }
        });
    }


}