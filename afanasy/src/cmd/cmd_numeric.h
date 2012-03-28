#pragma once

#include "cmd.h"

class CmdNumeric : public Cmd
{
public:
	CmdNumeric();
	~CmdNumeric();
	bool processArguments( int argc, char** argv, af::Msg &msg);
};

class CmdNumericGen : public Cmd
{
public:
	CmdNumericGen();
	~CmdNumericGen();
	bool processArguments( int argc, char** argv, af::Msg &msg);
};

class CmdNumericCmd : public Cmd
{
public:
	CmdNumericCmd();
	~CmdNumericCmd();
	bool processArguments( int argc, char** argv, af::Msg &msg);
};

class CmdNumericCalcTask : public Cmd
{
public:
	CmdNumericCalcTask();
	~CmdNumericCalcTask();
	bool processArguments( int argc, char** argv, af::Msg &msg);
};
