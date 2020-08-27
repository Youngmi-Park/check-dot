package com.example.checkdot.ReportBoard;

import androidx.appcompat.app.AppCompatActivity;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageButton;
import android.widget.TextView;

import com.example.checkdot.R;
import com.example.checkdot.ReportForm.ReportformActivity;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

//게시글의 제목과 날짜를 가져오는
public class BoardActivity extends AppCompatActivity {

    SwipeRefreshLayout mSwipeRefreshLayout;//새로고침
    TextView errorVeiw;
    WebView mWebView;

    private static String IP_ADD = "sphub.dothome.co.kr"; //ip주소
    private static String TAG = "MY LOG";//디버깅 태그

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_board);

        mSwipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.refreshView);
        mSwipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                mWebView.reload();
            }
        });


        errorVeiw = (TextView) findViewById(R.id.error_msg);
        mWebView = (WebView) findViewById(R.id.board_webview);

        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        mWebView.setWebViewClient(new WebViewClient() {

            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);

                mSwipeRefreshLayout.setRefreshing(false);
            }
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }

            //네트워크연결에러
            @Override
            public void onReceivedError(WebView view, int errorCode,String description, String failingUrl) {
                switch(errorCode) {
                    case ERROR_AUTHENTICATION: break;               // 서버에서 사용자 인증 실패
                    case ERROR_BAD_URL: break;                           // 잘못된 URL
                    case ERROR_CONNECT: break;                          // 서버로 연결 실패
                    case ERROR_FAILED_SSL_HANDSHAKE: break;    // SSL handshake 수행 실패
                    case ERROR_FILE: break;                                  // 일반 파일 오류
                    case ERROR_FILE_NOT_FOUND: break;               // 파일을 찾을 수 없습니다
                    case ERROR_HOST_LOOKUP: break;           // 서버 또는 프록시 호스트 이름 조회 실패
                    case ERROR_IO: break;                              // 서버에서 읽거나 서버로 쓰기 실패
                    case ERROR_PROXY_AUTHENTICATION: break;   // 프록시에서 사용자 인증 실패
                    case ERROR_REDIRECT_LOOP: break;               // 너무 많은 리디렉션
                    case ERROR_TIMEOUT: break;                          // 연결 시간 초과
                    case ERROR_TOO_MANY_REQUESTS: break;     // 페이지 로드중 너무 많은 요청 발생
                    case ERROR_UNKNOWN: break;                        // 일반 오류
                    case ERROR_UNSUPPORTED_AUTH_SCHEME: break; // 지원되지 않는 인증 체계
                    case ERROR_UNSUPPORTED_SCHEME: break;          // URI가 지원되지 않는 방식

                }
                super.onReceivedError(view, errorCode, description, failingUrl);
                mWebView.setVisibility(View.GONE);
                errorVeiw.setVisibility(View.VISIBLE);
            }
        });

        mWebView.loadUrl("http://access-lab.org/achievement/%ec%b2%b4%ed%81%ac%eb%8b%b7-%ed%9b%bc%ec%86%90-%ec%a0%90%ec%9e%90-%ec%8b%a0%ea%b3%a0-%ea%b2%8c%ec%8b%9c%ed%8c%90/");

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

        //+버튼, 게시글 추가
        final FloatingActionButton writeBtn = (FloatingActionButton)findViewById(R.id.writeBtn);
        writeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), ReportformActivity.class);
                startActivity(intent);
                //슬라이드 효과
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
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
