package com.example.checkdot.AboutUs;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

import com.example.checkdot.R;

public class AboutActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);

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
    //뒤로가기 키를 눌렀을 때 애니메이션 효과와 취소기능
    @Override
    public void onBackPressed() {
        finish();
        overridePendingTransition(R.anim.hold, R.anim.slide_right);
        // 코드 작성
        super.onBackPressed();
    }
}
