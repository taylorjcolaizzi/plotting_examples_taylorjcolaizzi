// This code may be compiled to make a stand alone exe
// or it can be run from the ROOT command line as:

// root [0] .L cpp_example.cpp  or .L cpp_example.cpp+
// root [1] cpp_example

// add comment here

#include "TApplication.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TRandom3.h"
//#include <cstdlib>
//#include <cmath>
//#include <iostream>

using namespace std;
using namespace ROOT::Math;


// examples of various plots in C++ program
void cpp_example(int samples=10000){
  // gStyle->SetOptStat(0);  // turn off default stats box in histograms

  // Histogram filled with a normal distribution
  auto tr = new TRandom3();
  auto hist1 = new TH1F("hist1","random gauss;x;frequency",100,50,150);
  auto fpeak = new TF1("fpeak","exp(-0.5*(x-[0])*(x-[0])/[1]/[1])",50,150);
  fpeak->SetParameters(100,6);
  hist1->FillRandom("fpeak",samples);
  auto tc1 = new TCanvas("c1","Canvas1");
  hist1->Draw("e");
  tc1->Update();

  // A multi panel plot
  auto tc2=new TCanvas("c2","Canvas2");
  tc2->Divide(2,2);  // divide in to 2x2 panels
  tc2->cd(1);
  hist1->Draw("e");

  // add a random uniform offset to the histogram
  auto hist2 = (TH1F*) hist1->Clone("hist2");
  hist2->SetTitle("Gauss+offset;x;frequency");
  for (int i=0; i<samples/3; ++i){
    hist2->Fill(tr->Uniform(50,150));
  }
  tc2->cd(2);
  hist2->Draw("e");

  // apply an offset to give us a 1/x^2 baseline
  auto hist3 = (TH1F*) hist1->Clone("hist3");
  hist3->SetTitle("Gauss+offset2;x;frequency");
  auto base2 = new TF1("base2","1/x/x",1,11);
  for (int i=0; i<samples*30; ++i){
    double x = base2->GetRandom()*10+40;
    hist3->Fill(x);
  }
  tc2->cd(3)->SetLogy();
  hist3->Draw("e");

  // a double gaussian
  auto hist4 = (TH1F*) hist1->Clone("hist4");
  hist4->SetTitle("Double Gaussian;x;frequency");
  fpeak->SetParameter(1,20);
  hist4->FillRandom("fpeak",samples/2);
  tc2->cd(4);
  hist4->Draw("e");

  tc2->Update();

  // example for saving our plot outputs in different formats
  tc1->SaveAs("canvas1.png");
  tc2->SaveAs("canvas2.pdf");
  
}

int main(int argc, char **argv) {
  int nsamples=10000;  // set sample sizes

  // This allows you to view ROOT-based graphics in your C++ program
  // If you don't want view graphics (eg just read/process/write data files), 
  // this can be ignored
  TApplication theApp("App", &argc, argv);

  if (argc>1) nsamples=atoi(argv[1]);
  
  cpp_example(nsamples);

  // view graphics in ROOT if we are in an interactive session
  if (!gROOT->IsBatch()) {
      cout << "To exit, quit ROOT from the File menu of the plot (or use control-C)" << endl;
    theApp.SetIdleTimer(30,".q"); // set up a failsafe timer to end the program
    theApp.Run(true);
  }
  return 0;
}
  
