package com.example.checkdot.ReportForm;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageButton;
import android.widget.TextView;
import com.example.checkdot.R;


public class ReportformActivity extends AppCompatActivity {

    private static String TAG = "MY LOG";//

    TextView errorVeiw;
    WebView mWebView;
    SwipeRefreshLayout mSwipeRefreshLayout;//새로고침

    ValueCallback mFilePathCallback;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reportform);
        mSwipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.refreshView);
        mSwipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                mWebView.reload();
            }
        });


        errorVeiw = (TextView) findViewById(R.id.error_msg);
        mWebView = (WebView) findViewById(R.id.form_webview);

        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        //사진 및 파일 업로드 권한 부여
        mWebView.setWebChromeClient(new WebChromeClient(){
            @Override
            public boolean onShowFileChooser(WebView webView, ValueCallback filePathCallback, FileChooserParams fileChooserParams) {
                mFilePathCallback = filePathCallback;

                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.setType("image/*");

                startActivityForResult(intent, 0);
                return true;
            }
        });
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

        mWebView.loadUrl("http://access-lab.org/achievement/%ec%b2%b4%ed%81%ac%eb%8b%b7-%ed%9b%bc%ec%86%90-%ec%a0%90%ec%9e%90-%ec%8b%a0%ea%b3%a0-%ea%b2%8c%ec%8b%9c%ed%8c%90/?mod=editor&pageid=1");


        //뒤로가기 버튼
        ImageButton undoBtn = (ImageButton)findViewById(R.id.undoBtn);
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
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        Log.e("resultCode:: ", String.valueOf(resultCode));
        if(requestCode == 0 && resultCode == Activity.RESULT_OK){
            if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
                mFilePathCallback.onReceiveValue(WebChromeClient.FileChooserParams.parseResult(resultCode, data));
            }else{
                mFilePathCallback.onReceiveValue(new Uri[]{data.getData()});
            }
            mFilePathCallback = null;
        }else{
            mFilePathCallback.onReceiveValue(null);
        }
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
