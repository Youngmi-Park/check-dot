package com.example.checkdot.Help;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ScrollView;

import com.example.checkdot.R;

public class HelpActivity extends AppCompatActivity {

    int pageNum;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_help);

        //이전 다음 버튼
        final Button nextBtn = findViewById(R.id.nextBtn);
        final Button backBtn = findViewById(R.id.backBtn);

        //페이지별 스크롤뷰
        final ScrollView page1 = findViewById(R.id.page1);
        final ScrollView page2 = findViewById(R.id.page2);
        final ScrollView page3 = findViewById(R.id.page3);
        final ScrollView page4 = findViewById(R.id.page4);
        final ScrollView page5 = findViewById(R.id.page5);

        //페이지 표시 버튼
        final Button view1 = findViewById(R.id.view1);
        final Button view2 = findViewById(R.id.view2);
        final Button view3 = findViewById(R.id.view3);
        final Button view4 = findViewById(R.id.view4);
        final Button view5 = findViewById(R.id.view5);

        pageNum=1;
        //다음 버튼을 눌렀을 때
        nextBtn.setOnClickListener(new View.OnClickListener() {
            @Override
                public void onClick(View v) {
                Log.d("숫자가 뭐지", "onClick: "+pageNum);
                switch (pageNum){
                    case 1:
                    //페이지가 바뀜
                    page1.setVisibility(View.GONE);
                    page2.setVisibility(View.VISIBLE);

                    //페이지 표시가 바뀜
                    view1.setBackgroundResource(R.drawable.disable_page_theme);
                    view2.setBackgroundResource(R.drawable.recent_page_theme);

                    //이전 버튼 보이게
                    backBtn.setVisibility(View.VISIBLE);
                    backBtn.setClickable(true);
                    pageNum=2;
                    break;

                    case 2:
                    //페이지가 바뀜
                    page2.setVisibility(View.GONE);
                    page3.setVisibility(View.VISIBLE);

                    //페이지 표시가 바뀜
                    view2.setBackgroundResource(R.drawable.disable_page_theme);
                    view3.setBackgroundResource(R.drawable.recent_page_theme);
                    pageNum=3;
                    break;

                    case 3:
                    //페이지가 바뀜
                    page3.setVisibility(View.GONE);
                    page4.setVisibility(View.VISIBLE);

                    //페이지 표시가 바뀜
                    view3.setBackgroundResource(R.drawable.disable_page_theme);
                    view4.setBackgroundResource(R.drawable.recent_page_theme);
                    pageNum=4;
                    break;

                    case 4:
                        //다음 버튼이 사라짐
                    nextBtn.setVisibility(View.INVISIBLE);
                    nextBtn.setClickable(false);

                    //페이지가 바뀜
                    page4.setVisibility(View.GONE);
                    page5.setVisibility(View.VISIBLE);

                    //페이지 표시가 바뀜
                    view4.setBackgroundResource(R.drawable.disable_page_theme);
                    view5.setBackgroundResource(R.drawable.recent_page_theme);
                    pageNum=5;
                    break;
               }
            }
        });

        backBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switch (pageNum){
                    case 2:
                    //이전버튼 사라짐.
                    backBtn.setVisibility(View.INVISIBLE);
                    backBtn.setClickable(false);

                    //페이지 바뀜
                    page1.setVisibility(View.VISIBLE);
                    page2.setVisibility(View.GONE);

                    //페이지 표시 바뀜
                    view1.setBackgroundResource(R.drawable.recent_page_theme);
                    view2.setBackgroundResource(R.drawable.disable_page_theme);
                    pageNum=1;
                    break;

                    case 3:
                    //페이지 바뀜
                    page2.setVisibility(View.VISIBLE);
                    page3.setVisibility(View.GONE);

                    //페이지 표시 바뀜
                    view2.setBackgroundResource(R.drawable.recent_page_theme);
                    view3.setBackgroundResource(R.drawable.disable_page_theme);

                    pageNum=2;
                    break;

                    case 4:
                    //페이지 바뀜
                    page3.setVisibility(View.VISIBLE);
                    page4.setVisibility(View.GONE);

                    //페이지 표시 바뀜
                    view3.setBackgroundResource(R.drawable.recent_page_theme);
                    view4.setBackgroundResource(R.drawable.disable_page_theme);

                    pageNum=3;
                    break;

                    case 5:
                    //페이지 바뀜
                    page4.setVisibility(View.VISIBLE);
                    page5.setVisibility(View.GONE);

                    //페이지 표시 바뀜
                    view4.setBackgroundResource(R.drawable.recent_page_theme);
                    view5.setBackgroundResource(R.drawable.disable_page_theme);

                    //다음버튼이 나타남.
                    nextBtn.setVisibility(View.VISIBLE);
                    nextBtn.setClickable(true);

                    pageNum=4;

                }
            }
        });



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
