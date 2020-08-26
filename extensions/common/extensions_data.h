/*
struct CrxInfo
{
  const char* id;
  const char* name;
  const char* version;
  bool hidden;
  bool can_disable;
};
*/

static extensions::CrxInfo crx_array[] = { };

static int crx_array_size = 0;

static const char* ext_force_from_store[] = { };

static int ext_force_from_store_size = 0;