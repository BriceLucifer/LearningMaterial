# learing_material
1. leetcode once a day
2. try to read CSAPP
3. learn cpp and nvidia constantly

# 如何在mac添加自己的ssh密钥
    ssh-keygen -t ed25519 -C "your_email@example.com"
# 然后会选择名字 自己在name写一个喜欢的就行 剩下的enter


# 第三个在你的.ssh/config
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/文件名

# 第四部
ssh-add --apple-use-keychain ~/.ssh/文件名

# 克隆仓库 然后在你的仓库配置名字和email不要添加--global
git config user.name "你的github昵称"
git config user.email "xxx邮箱"
z
