noDragon = []
doDragon = []
oneDay = []
twoDay = []

for(var i = 0; i < 60; i++) {
    noDragon.push(0);
    doDragon.push(0);
    oneDay.push(0);
    twoDay.push(0);
}
oneDay[0] = 1;
for(var i = 1; i < 46; i++) {
    twoDay[i] += oneDay[i-1];
    doDragon[i] += twoDay[i-1]
    doDragon[i+1] += twoDay[i-1]
    doDragon[i+2] += twoDay[i-1]
    doDragon[i+3] += twoDay[i-1]
    for(var j = i+4; j < 60; j++)
        noDragon[j] += twoDay[i-1]
    oneDay[i] = doDragon[i]
}

console.log(noDragon);
for(var i = 0; i < 50; i++)
{
    s = oneDay[i] + twoDay[i]
    console.log(i + " - no :" + noDragon[i] + " do :" + doDragon[i] + " eggs : "  + s);
}
console.log(doDragon);