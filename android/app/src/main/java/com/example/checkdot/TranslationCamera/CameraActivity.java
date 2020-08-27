package com.example.checkdot.TranslationCamera;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.core.content.FileProvider;

import android.Manifest;
import android.app.ProgressDialog;
import android.content.ComponentName;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.graphics.Bitmap;
import android.graphics.Camera;
import android.media.MediaScannerConnection;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.checkdot.MainActivity;
import com.example.checkdot.R;
import com.example.checkdot.ReportForm.ReportformActivity;
import com.yalantis.ucrop.UCrop;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.channels.FileChannel;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

/*어플의 메인기능을 하는 부분
1.카메라로 사진 촬영
2.앨범에서 사진가져오기
3.이미지 서버로 사진 전송
*/
public class CameraActivity extends AppCompatActivity implements View.OnClickListener {

    private ImageView imgMain;
    private Button btnCamera, btnUpload;

    private static final String CROPPED_IMAGE = "CheckDot_";

    private static final int PICK_FROM_CAMERA = 1;
    private static final int PICK_FROM_ALBUM = 2;
    private static final int CROP_FROM_CAMERA = 69;

    private Uri photoUri;
    private String[] permissions = {Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE,
            Manifest.permission.CAMERA};
    private static final int MULTIPLE_PERMISSIONS = 101;

    String uploadFilePath;
    String uploadFIleUri;

    TextView messageText;
    LinearLayout noticeMessage;
    TextView selectMessage;
    CustomPhotoDialog photoDialog;
    View.OnClickListener cameraListener, albumListener;

    int serverResponseCode = 0;
    String upLoadServerUri = "http://sphub.dothome.co.kr/UploadToServer.php";//서버컴퓨터의 ip주소


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
        checkPermissions();
        initView();

        cameraListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                takePhoto();
            }
        };
        albumListener = new View.OnClickListener() {
            @Override
            public void onClick(View dialog) {
                goToAlbum();
            }
        };
        photoDialog = new CustomPhotoDialog(CameraActivity.this);

        selectMessage = (TextView)findViewById(R.id.selectMessage);
        noticeMessage = (LinearLayout)findViewById(R.id.noticeMessage);

        //신고하기 버튼
        final Button reportBtn = (Button)findViewById(R.id.reportBtn);
        reportBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplication(), ReportformActivity.class);
                startActivity(intent);
                //슬라이드 효과
                overridePendingTransition(R.anim.slide_left, R.anim.hold);
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
    //버튼 클릭리스너
    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.takeBtn:
                //커스텀 다이얼로그 생성
                photoDialog.DialogFunction(cameraListener,albumListener);
                break;
            case R.id.uploadBtn:
                //3.사진 서버로 전송
                if(photoUri!= null){
                    //사진이 있을때만 동작하도록 설정
                    uploadPhoto();
                }else{
                    Toast.makeText(this, "번역할 점자 사진이 없습니다.", Toast.LENGTH_SHORT).show();
                }
                break;
        }
    }

    //퍼미션 확인하는 부분
    private boolean checkPermissions() {
        int result;
        List<String> permissionList = new ArrayList<>();
        for (String pm : permissions) {
            result = ContextCompat.checkSelfPermission(this, pm);
            if (result != PackageManager.PERMISSION_GRANTED) {
                permissionList.add(pm);
            }
        }
        if (!permissionList.isEmpty()) {
            ActivityCompat.requestPermissions(this, permissionList.toArray(new String[permissionList.size()]), MULTIPLE_PERMISSIONS);
            return false;
        }
        return true;
    }

    //뷰 초기화
    private void initView() {
        //이미지 뷰와 버튼을 가져와서 클릭리스너를 달아줌.
        imgMain = findViewById(R.id.photo);
        btnCamera = findViewById(R.id.takeBtn);
        btnUpload = findViewById(R.id.uploadBtn);
        messageText  = findViewById(R.id.messageText);

        btnCamera.setOnClickListener(this);
        btnUpload.setOnClickListener(this);
//        messageText.setText("Uploading file path :- '");
    }

    //1.사진 촬영
    private void takePhoto() {
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        File photoFile = null;
        try {
            photoFile = createImageFile();
        } catch (IOException e) {
            Toast.makeText(CameraActivity.this, "이미지 처리 오류! 다시 시도해주세요.", Toast.LENGTH_SHORT).show();
            finish();
            e.printStackTrace();
        }
        if (photoFile != null) {
            photoUri = null;
            photoUri = FileProvider.getUriForFile(CameraActivity.this, "com.example.checkdot.provider", photoFile);
            intent.putExtra(MediaStore.EXTRA_OUTPUT, photoUri);
            startActivityForResult(intent, PICK_FROM_CAMERA);
        }
        photoDialog.DismissDialog();
    }

    //2.앨범 열기
    private void goToAlbum() {
        Intent intent = new Intent(Intent.ACTION_PICK);
        intent.setType(MediaStore.Images.Media.CONTENT_TYPE);
        startActivityForResult(intent, PICK_FROM_ALBUM);
        photoDialog.DismissDialog();
    }

    //3.사진 서버로 전송
    private void uploadPhoto() {
        new Thread(new Runnable() {
            public void run() {
                runOnUiThread(new Runnable() {
                    public void run() {
                        messageText.setText(". . . 업로드 중. . .");
                    }
                });
                Log.d("TAGdd", "uploadFIle Uri: "+uploadFIleUri+ "uploadfile path"+uploadFilePath);
                uploadFile(uploadFIleUri);
            }

        }).start();
    }

    //이미지 경로 생성
    private File createImageFile() throws IOException {
        String timeStamp = new SimpleDateFormat("HHmmss").format(new Date());
        String imageFileName = "CheckDot_" + timeStamp + "_";

        //새로운 폴더 생성, 있으면 만들지 않고 없으면 만듬
        File storageDir = new File(Environment.getExternalStorageDirectory() + "/CheckDot/");
        if (!storageDir.exists()) {
            storageDir.mkdirs();
        }
        File image = File.createTempFile(imageFileName, ".jpg", storageDir);
        uploadFilePath = storageDir.toString();
        Log.d("TAGdd",  "uploadfile path"+uploadFilePath);

        return image;
    }

    //이미지 크롭하기
    public void cropImage() {
        this.grantUriPermission("com.android.camera", photoUri,Intent.FLAG_GRANT_WRITE_URI_PERMISSION | Intent.FLAG_GRANT_READ_URI_PERMISSION);
        Intent intent = new Intent("com.android.camera.action.CROP");
        intent.setDataAndType(photoUri, "image/*");
        List<ResolveInfo> list = getPackageManager().queryIntentActivities(intent, 0);
        grantUriPermission(list.get(0).activityInfo.packageName, photoUri, Intent.FLAG_GRANT_WRITE_URI_PERMISSION | Intent.FLAG_GRANT_READ_URI_PERMISSION);

        int size = list.size();
        if (size == 0) {
            Toast.makeText(this, "취소 되었습니다.", Toast.LENGTH_SHORT).show();
            return;
        } else {
            Toast.makeText(this, "용량이 큰 사진의 경우 시간이 오래 걸릴 수 있습니다.", Toast.LENGTH_SHORT).show();
            intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
            intent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
            intent.putExtra("crop", "true");
            intent.putExtra("scale", true);

            File croppedFileName = null;

            try {
                croppedFileName = createImageFile();
            } catch (IOException e) {
                e.printStackTrace();
            }

            File folder = new File(Environment.getExternalStorageDirectory() + "/CheckDot/");
            File tempFile = new File(folder.toString(), croppedFileName.getName());
//            Log.d("TAGdd", croppedFileName.getName());

            uploadFIleUri = uploadFilePath+"/"+croppedFileName.getName();
            photoUri = FileProvider.getUriForFile(CameraActivity.this,getPackageName()+".provider", tempFile);

            intent.putExtra("return-data", false);
            intent.putExtra(MediaStore.EXTRA_OUTPUT, photoUri);
            intent.putExtra("outputFormat", Bitmap.CompressFormat.JPEG.toString());

            Intent i = new Intent(intent);
            ResolveInfo res = list.get(0);
            grantUriPermission(res.activityInfo.packageName, photoUri, Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
            i.setComponent(new ComponentName(res.activityInfo.packageName, res.activityInfo.name));
            startActivityForResult(i, CROP_FROM_CAMERA);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {
        switch (requestCode) {
            case MULTIPLE_PERMISSIONS: {
                if (grantResults.length > 0) {
                    for (int i = 0; i < permissions.length; i++) {
                        if (permissions[i].equals(this.permissions[0])) {
                            if (grantResults[i] != PackageManager.PERMISSION_GRANTED) {
                                showNoPermissionToastAndFinish();
                            }
                        } else if (permissions[i].equals(this.permissions[1])) {
                            if (grantResults[i] != PackageManager.PERMISSION_GRANTED) {
                                showNoPermissionToastAndFinish();

                            }
                        } else if (permissions[i].equals(this.permissions[2])) {
                            if (grantResults[i] != PackageManager.PERMISSION_GRANTED) {
                                showNoPermissionToastAndFinish();

                            }
                        }
                    }
                } else {
                    showNoPermissionToastAndFinish();
                }
                return;
            }
        }
    }

    private void showNoPermissionToastAndFinish() {
        Toast.makeText(this, "권한 요청에 동의 해주셔야 이용 가능합니다. 설정에서 권한 허용 하시기 바랍니다.", Toast.LENGTH_SHORT).show();
        finish();
    }


    //사진 촬영 혹은 선택 후에 진행
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (resultCode != RESULT_OK) {
            Toast.makeText(this, "취소 되었습니다.", Toast.LENGTH_SHORT).show();
            return;
        }
        //앨범에서 사진 선택
        if (requestCode == PICK_FROM_ALBUM) {
            if (data == null) {
                return;
            }
            photoUri = data.getData();
            //이미지 자르기
            startCrop(photoUri);
      //      cropImage();
        } else if (requestCode == PICK_FROM_CAMERA) {
            //사진 촬영인 경우
            startCrop(photoUri);

//            cropImage();
            // 갤러리에 나타나게
            MediaScannerConnection.scanFile(CameraActivity.this,
                    new String[]{photoUri.getPath()}, null,
                    new MediaScannerConnection.OnScanCompletedListener() {
                        public void onScanCompleted(String path, Uri uri) {
                        }
                    });
        } else if (requestCode == CROP_FROM_CAMERA) {
            //편집한 이미지 Uri
            photoUri = UCrop.getOutput(data);

            //편집한 이미지 저장
            copyFileToDownloads(photoUri);

            //이미지 UI에 업로드
            selectMessage.setVisibility(View.GONE);
            imgMain.setImageURI(null);
            imgMain.setImageURI(UCrop.getOutput(data));
            revokeUriPermission(photoUri, Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
        }
    }


    private void copyFileToDownloads(Uri resultUri) {
        //권한 확인
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {
//            requestPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE,
//                    getString(R.string.permission_write_storage_rationale),
//                    REQUEST_STORAGE_WRITE_ACCESS_PERMISSION);
        } else {
            if (resultUri != null && resultUri.getScheme().equals("file")) {
                try {
                    String timeStamp = new SimpleDateFormat("HHmmss").format(new Date());
                    String filename = "CheckDot_" + timeStamp + ".jpg";

                    //새로운 폴더 생성, 있으면 만들지 않고 없으면 만듦
                    File storageDir = new File(Environment.getExternalStorageDirectory() + "/CheckDot/");
                    if (!storageDir.exists()) {
                        storageDir.mkdirs();
                    }

                    uploadFilePath = storageDir.toString();
                    uploadFIleUri = uploadFilePath+"/"+ filename;

                    //지정한 경로에 이미지 저장
                    File saveFile = new File(uploadFilePath, filename);

                    FileInputStream inStream = new FileInputStream(new File(resultUri.getPath()));
                    FileOutputStream outStream = new FileOutputStream(saveFile);
                    FileChannel inChannel = inStream.getChannel();
                    FileChannel outChannel = outStream.getChannel();
                    inChannel.transferTo(0, inChannel.size(), outChannel);
                    inStream.close();
                    outStream.close();

                } catch (Exception e) {
//                    Toast.makeText(ResultActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
//                    Log.e(TAG, imageUri.toString(), e);
                }
            } else {
                //Toast.makeText(ResultActivity.this, getString(R.string.toast_unexpected_error), Toast.LENGTH_SHORT).show();
            }
        }



    }

    private void startCrop(@NonNull Uri uri) {
        String destinationFileName = CROPPED_IMAGE;
        UCrop uCrop = UCrop.of(uri, Uri.fromFile(new File(getCacheDir(), destinationFileName)));

                                                        // else start uCrop Activity
            uCrop.start(CameraActivity.this);

    }

    public int uploadFile(String sourceFileUri) {
        String fileName = photoUri.toString();
        HttpURLConnection conn;
        DataOutputStream dos;

        String lineEnd = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";

        int bytesRead, bytesAvailable, bufferSize;
        byte[] buffer;
        int maxBufferSize = 1 * 1024 * 1024;

        File sourceFile = new File(uploadFIleUri);
        if (!sourceFile.isFile()) {
            runOnUiThread(new Runnable() {

                public void run() {
//                    messageText.setText("Source File not exist :"+photoUri.toString()+"/n filepath"+uploadFilePath+"/n uri"+uploadFIleUri);
                }
            });
            return 0;
        }
        else
        {
            try {
                // open a URL connection to the Servlet

                FileInputStream fileInputStream = new FileInputStream(sourceFile);
                URL url = new URL(upLoadServerUri);

                // Open a HTTP  connection to  the URL
                conn = (HttpURLConnection) url.openConnection();
                conn.setDoInput(true); // Allow Inputs
                conn.setDoOutput(true); // Allow Outputs
                conn.setUseCaches(false); // Don't use a Cached Copy
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Connection", "Keep-Alive");
                conn.setRequestProperty("ENCTYPE", "multi.part/form-data");
                conn.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
                conn.setRequestProperty("uploaded_file", fileName);

                dos = new DataOutputStream(conn.getOutputStream());
                dos.writeBytes(twoHyphens + boundary + lineEnd);
                dos.writeBytes("Content-Disposition: form-data; name=\"uploaded_file\";filename=\""

                        + fileName + "\"" + lineEnd);
                dos.writeBytes(lineEnd);

                // create a buffer of  maximum size
                bytesAvailable = fileInputStream.available();
                bufferSize = Math.min(bytesAvailable, maxBufferSize);
                buffer = new byte[bufferSize];

                // read file and write it into form...
                bytesRead = fileInputStream.read(buffer, 0, bufferSize);

                while (bytesRead > 0) {
                    dos.write(buffer, 0, bufferSize);
                    bytesAvailable = fileInputStream.available();
                    bufferSize = Math.min(bytesAvailable, maxBufferSize);
                    bytesRead = fileInputStream.read(buffer, 0, bufferSize);
                }
                // send multipart form data necesssary after file data...
                dos.writeBytes(lineEnd);
                dos.writeBytes(twoHyphens + boundary + twoHyphens + lineEnd);

                // Responses from the server (code and message)
                serverResponseCode = conn.getResponseCode();
                String serverResponseMessage = conn.getResponseMessage();
                Log.i("uploadFile", "HTTP Response is : "
                        + serverResponseMessage + ": " + serverResponseCode);

                BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                final StringBuilder sb = new StringBuilder();
                String line;
                while((line=br.readLine())!=null){
                    sb.append(line);
                }
                if(serverResponseCode == 200){
                    runOnUiThread(new Runnable() {

                        public void run() {
                            Toast.makeText(CameraActivity.this, "번역 중 입니다.",
                                    Toast.LENGTH_SHORT).show();
                            //번역 결과 텍스트, 폰트사이즈
                            messageText.setText(sb);
                            messageText.setTextSize(20);
                            //해석후에 해석결과에 대한 경고 메시지 나타남
                            noticeMessage.setVisibility(View.VISIBLE);
                        }

                    });
                }
                //close the streams //
                fileInputStream.close();
                dos.flush();
                dos.close();

            } catch (MalformedURLException ex) {
                ex.printStackTrace();

                runOnUiThread(new Runnable() {

                    public void run() {
                    //    messageText.setText("MalformedURLException Exception : check script url.");
                        Toast.makeText(CameraActivity.this, "MalformedURLException",
                                Toast.LENGTH_SHORT).show();
                    }

                });
                Log.e("Upload file to server", "error: " + ex.getMessage(), ex);

            } catch (Exception e) {
                e.printStackTrace();

                runOnUiThread(new Runnable() {

                    public void run() {
                    //    messageText.setText("Got Exception : see logcat ");
                        Toast.makeText(CameraActivity.this, "Got Exception : see logcat ",
                                Toast.LENGTH_SHORT).show();
                    }

                });
                Log.e("server Exception", "Exception : " + e.getMessage(), e);
            }
            return serverResponseCode;
        } // End else block
    }
}