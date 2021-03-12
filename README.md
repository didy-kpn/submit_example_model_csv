# submit_example_model_csv

I used following article as reference to automate submission to numerai.

It is possible to submit the example model by simply execute this program.

[Numeraiに上位20%以上のスコアがでる予測値を提出する方法](https://qiita.com/tit_BTCQASH/items/4b321f06f7fea9709e05)

# How to use

## Set your API keys and Model ID

before execute it, need to write API key and model ID in a configuration file or environment variable.

"dest_path" and "NUMERAI_DEST_PATH" accept NULL, empty or unspecified, in which case the tournament dataset will be downloaded to the current directory.

### if you want to set configuration file


```shell
$ cat config.yml
---
public_id: ~
secret_key: ~
model_id: ~
dest_path: ~
$ vim config.yml
```

### if you want to set environment variable

```shell
$ export NUMERAI_PUBLIC_ID=REPLACE;
$ export NUMERAI_SECRET_KEY=REPLACE;
$ export NUMERAI_MODEL_ID=REPLACE;
$ export NUMERAI_DEST_PATH=;
```

## execute python file

This is the last part. Just execute it to download the new dataset and submit the example model.

```shell
$ python example_predictions.py
```

NMR: 0x0000000000000000000000000000000000023ead

# License

This project is licensed under the MIT License.

See [LICENSE](https://github.com/didy-kpn/submit_example_model_csv/blob/master/LICENSE) for details.
