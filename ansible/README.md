## ansibleによるデブロイ自動化手順

### 0. macにansible環境を構築

http://qiita.com/msrks/items/e0de2931ef726448696d

### 1. playbookを実行する

下記コマンンドを実行する

```
$ ansible-playbook -i hosts playbook.yml
```

NGがなくなるまで下記コマンドを繰り返し実行する

```
$ ansible-playbook -i hosts playbook.yml --limit @/Users/riki/githubrepo/socket-app/ansible/playbook.retry
```

### 2. sudo権限が必要なplaybookを実行する

下記コマンンドを実行する

```
$ ansible-playbook -i hosts playbook_sudo.yml
```

NGがなくなるまで下記コマンドを繰り返し実行する

```
$ ansible-playbook -i hosts playbook_sudo.yml --limit @/Users/riki/githubrepo/socket-app/ansible/playbook_sudo.retry
```
