double rnd40_64()
{
static long long int u[2] = { 1, 0 };
static const long long int m[2] = { 45887173, 11368 };
static const double x[2] = {
pow(2.0, -40.0),
pow(2.0, -14.0)
};
long long int n, c0, c1;

c0 = m[0] * u[0];
c1 = m[0] * u[1] + m[1] * u[0];

u[0] = c0 - ((c0 >> 26) << 26);
n = c1 + (c0 >> 26);
u[1] = n - ((n >> 14) << 14);

return u[0] * x[0] + u[1] * x[1];
}