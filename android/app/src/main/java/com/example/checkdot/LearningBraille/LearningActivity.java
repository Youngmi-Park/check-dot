package com.example.checkdot.LearningBraille;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentStatePagerAdapter;
import androidx.viewpager.widget.PagerAdapter;
import androidx.viewpager.widget.ViewPager;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.LinearLayout;

import com.example.checkdot.R;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.IOException;

public class LearningActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_learning);


        //뒤로가기 버튼
        final ImageButton undoBtn = (ImageButton)findViewById(R.id.undoBtn);
        undoBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //엑티비티 종료
                finish();
                overridePendingTransition(R.anim.hold, R.anim.slide_right);
            }
        });
    }
    @Override
    public void onBackPressed() {
            finish();
            overridePendingTransition(R.anim.hold, R.anim.slide_right);
            super.onBackPressed();
    }
}