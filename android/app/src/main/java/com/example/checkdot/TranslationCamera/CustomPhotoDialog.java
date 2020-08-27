package com.example.checkdot.TranslationCamera;

import android.app.AlertDialog;
import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.graphics.drawable.ColorDrawable;
import android.util.DisplayMetrics;
import android.view.ContextThemeWrapper;
import android.view.Gravity;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.TextView;

import com.example.checkdot.R;

import static androidx.fragment.app.DialogFragment.STYLE_NORMAL;

public class CustomPhotoDialog {
    private Context context;
    Dialog dialog;

    public CustomPhotoDialog(Context context){
        this.context=context;
    }

    //custom dialog 호출 함수
        public void DialogFunction(final View.OnClickListener photoFunc, final View.OnClickListener albumFunc){
            //커스텀을 위한 dialog 클래스 생성
            dialog = new Dialog(context);
            //다이얼로그 제목 부분없앰
            dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
            //아래쪽에 위치하도록 지정
            dialog.getWindow().setGravity(Gravity.BOTTOM);
            //가로사이즈 조절
            WindowManager.LayoutParams lp = new WindowManager.LayoutParams();
        lp.copyFrom(dialog.getWindow().getAttributes());
        lp.width = WindowManager.LayoutParams.MATCH_PARENT;
        lp.height = WindowManager.LayoutParams.MATCH_PARENT;
        //다이얼로그 레이아웃 설정
        dialog.setContentView(R.layout.custom_photo_dialog);


        dialog.show();
        dialog.getWindow().setAttributes(lp);
        //배경 투명하게
        dialog.getWindow().setBackgroundDrawable(new ColorDrawable(0x66000000));
        dialog.getWindow().getAttributes().windowAnimations = R.style.DialogAnimation;


        final View view = (View)dialog.findViewById(R.id.view);
        final TextView photoBtn = (TextView)dialog.findViewById(R.id.photoBtn);
        final TextView albumBtn = (TextView)dialog.findViewById(R.id.albumBtn);
        final TextView cancelBtn = (TextView)dialog.findViewById(R.id.cancelBtn);

       // photoBtn.setWidth(lp.width);
        photoBtn.setOnClickListener(photoFunc);
        albumBtn.setOnClickListener(albumFunc);
        view.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                dialog.dismiss();
            }
        });
        cancelBtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                //다이얼로그 종료
                dialog.dismiss();
            }
        });
    }
    public void DismissDialog(){
        dialog.dismiss();
    }
}
