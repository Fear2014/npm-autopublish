set package=%1
echo %package%
call npm install %package% --registry http://npm.com:4873

cd node_modules\%package%


setlocal enabledelayedexpansion
REM 声明采用UTF-8编码
chcp 65001
for /f "delims=" %%a in (package.json) do (
set var=%%a
set var=!var:Dow=fear!
set var=!var:oldnpm.com=npm.cn!
echo/ !var!>>"package.json._"
)

move /y "package.json._" "package.json"
copy ..\..\.gitignore .\
npm set registry http://targeturl:4873
npm publish registry http://targeturl:4873

cd ..\..\

rmdir /s/q node_modules
