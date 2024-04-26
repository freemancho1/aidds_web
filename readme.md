# AIDDS_WEB
AIDDS 중에서 모델을 이용해 웹에서 서비스하는 부분

<br/><br/>

## 제약 조건
* 연동되는 모든 `json데이터의 아이템명은 소문자`로 처리됨

<br/><br/>

## 프로그램 운영
### 프로그램 실행
* 프로그램을 실행하기 위해서는 `run`파일 1행에 실행 환경의 파이썬 프로그램을 연결해야 함
```python
#!/home/??/anaconda3/envs/aidds_web/bin/python
# ?? 부분을 포함해 전체 경로를 맞춰줘야 함
```

* `run`파일이 존재하는 폴더에서 실행(`기본 포트는 11002임`)
```terminal
> ./run
```
```terminal
> ./run -p 11000
```

<br/>

### 웹 서비스 요청
#### (배치) 공사비 예측 요청
```
http://localhost:11002/predict
```
* json data sample
```json
{"pred_1": {"cons": {"acc_no": "70HC20224688", "cons_cost": 3599115, "office_cd": "HHHH", "cntr_pwr": 3, "sply_tpcd": 1, "pred_id": "pred_1", "pred_seq": "pred_1"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}, "pole_2": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 18, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "D2", "sl_spec_cd": 3.2, "sl_span": 7, "sl_lico": 1}}}, "pred_2": {"cons": {"acc_no": "70HC20224688", "cons_cost": 2505760, "office_cd": "KKKK", "cntr_pwr": 3, "sply_tpcd": 1, "pred_id": "pred_2", "pred_seq": "pred_2"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 54, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "C2", "sl_spec_cd": 25.0, "sl_span": 6, "sl_lico": 1}}}, "pred_3": {"cons": {"acc_no": "70HC20224688", "cons_cost": 3212909, "office_cd": "BBBB", "cntr_pwr": 3, "sply_tpcd": 1, "pred_id": "pred_3", "pred_seq": "pred_3"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 32, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}, "line_2": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 39, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "D2", "sl_spec_cd": 3.2, "sl_span": 15, "sl_lico": 1}}}}
```
* 리턴값: 'cons' 아이템만 조금(예측공사비 포함) 변하고 입력받은 값 그대로 전송함
```json
{"pred_1": {"cons": {"acc_no": "70HC20224688", "cons_cost": 3481152, "pred_id": "pred_1", "pred_seq": "pred_1"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}, "pole_2": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 18, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "D2", "sl_spec_cd": 3.2, "sl_span": 7, "sl_lico": 1}}}, "pred_2": {"cons": {"acc_no": "70HC20224688", "cons_cost": 2578166, "pred_id": "pred_2", "pred_seq": "pred_2"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 54, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "C2", "sl_spec_cd": 25.0, "sl_span": 6, "sl_lico": 1}}}, "pred_3": {"cons": {"acc_no": "70HC20224688", "cons_cost": 2908765, "pred_id": "pred_3", "pred_seq": "pred_3"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 32, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}, "line_2": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 39, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "D2", "sl_spec_cd": 3.2, "sl_span": 15, "sl_lico": 1}}}}
```

<br/>

#### 변경 공사비 예측 요청
```
http://localhost:11002/re_predict
```
* json data sample
```json
{"pred_2": {"cons": {"acc_no": "70HC20224688", "cons_cost": 2505760, "office_cd": "KKKK", "cntr_pwr": 3, "sply_tpcd": 1, "pred_id": "pred_2", "pred_seq": "pred_2"}, "pole": {"pole_1": {"acc_no": "70HC20224688", "pole_form_cd": "O", "pole_knd_cd": "C", "pole_spec_cd": 10.0, "geo_x": "", "geo_y": ""}}, "line": {"line_1": {"acc_no": "70HC20224688", "wrng_mode_cd": 13, "span": 54, "wire_knd_cd": "AO", "wire_spec_cd": 35.0, "wire_lico": 1, "newi_knd_cd": "AL", "newi_spec_cd": 32.0}}, "sl": {"sl_1": {"acc_no": "70HC20224688", "sl_type_cd": "C2", "sl_spec_cd": 25.0, "sl_span": 6, "sl_lico": 1}}}}
```
* 리턴값: 'cons' 아이템만 전송
```json
{"acc_no": "70HC20224688", "cons_cost": 2578166, "pred_id": "pred_2", "pred_seq": "pred_2"}
```

<br/><br/>

## 폴더 설명
### /
시스템 실행, 가상환경 설치 라이브러리, RESTAPI 서버 정의
* run: 시스템 실행파일
* restapi_server.py: RESTAPI 서버 정의
* requirements.aidds_web.txt: 가상환경 aidds_web에 설치할 라이브러리 정의
* readme.md: 시스템 설명 파일

<br/>

### /data
서비스 시점에 필요한 피클, 스케일러 및 모델 데이터가 있음
* model: `서비스에 사용할 모델` 저장(학습이 가장 잘 된 모델)
* pickle: `서비스에 사용할 피클 및 스케일러` 데이터

<br/>

### /service
서비스에 필요한 `예측 클래스(전처리 포함)`, `라우터` 및 `서비스메니저`로 구성
* predict.py: 서비스 예측 클래스, `최초 공사비 예측과 변경 경로에 대한 공사비 예측을 하나의 클래스로 처리`
  * _pp_module.py, _preprocessing.py: 전처리 모듈
* route.py: 서비스 라우터 정의 클래스들 모음, 최초 공사비 예측을 위한 라우터와 변경 공사비 예측을 위한 라우터가 분리되어 있음
* service_manager.py: `싱글톤 서비스`를 위한 서비스 메니저

<br/>

### /sys
시스템 실행에 필요한 기본 파일들
* args.py: 프로그램 실행 시 사용되는 인자를 받음(현재는 웹 포트 정보만 받고 있음)
* config.py, messages.py: `시스템 설정` 및 `사용할 메시지` 정보
* init.py: 최초 시스템 실행에 필요한 설정정보 처리(예외 무시 처리만 있음)
* http_codes.py: 웹 서비스에 필요한 http return code 정의

<br/>

### /utils
시스템 실행에 도움을 주는 기본적인 기능들이 구현되어 있음
* data_io.py: `데이터, 피클 및 모델을 저장하고 불러오는` 기능 구현
* exception.py: 시스템에서 사용하는 `사용자 정의 예외처리` 기능 구현
* logs.py: 시스템에서 사용하는 `로그 출력` 기능 구현
* trace.py: logs와 exception에서 사용하는 `에러 출력 함수와 코드를 찾는` 기능 구현
