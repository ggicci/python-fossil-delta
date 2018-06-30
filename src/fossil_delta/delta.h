int delta_analyze(const char *zDelta, int lenDelta, int *pnCopy, int *pnInsert);
int delta_apply(const char *zSrc, int lenSrc, const char *zDelta, int lenDelta, char *zOut);
int delta_output_size(const char *zDelta, int lenDelta);
int delta_create(const char *zSrc, unsigned int lenSrc, const char *zOut, unsigned int lenOut, char *zDelta);

void fossil_free(void *p);
void *fossil_malloc(size_t n);
void fossil_panic(const char *zFormat, ...);
typedef unsigned short int u16;
typedef short int s16;
typedef unsigned int u32;
