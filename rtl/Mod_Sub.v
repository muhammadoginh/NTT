`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Muhammad Ogin Hasanuddin
// 
// Create Date: 2024/02/07 10:56:10
// Design Name: 
// Module Name: Mod_Sub
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Mod_Sub(
    input clk,
    input rstn,
    input [47:0] A,
    input [47:0] M,
    input [47:0] q,
    output reg [47:0] B
    );
    
    reg [48:0] Sub;
    
    reg [47:0] in_A;
    reg [47:0] in_M;
    reg [47:0] in_q;
    reg [47:0] out_B;
    
    // register input
    always @(posedge clk or negedge rstn)
    begin
        if (~rstn)
        begin
            in_A <= 0;
            in_M <= 0;
            in_q <= 0;
        end
        else
        begin
            in_A <= A;
            in_M <= M;
            in_q <= q;
        end
    end
    
//    assign Sub = in_A - in_M;
    
    // Model 1
//    always @(*)
//    begin
//        if (Sub[48])
//            B = Sub + q;
//        else
//            B = Sub;
//    end
    
    // Model 2
    always @(*)
    begin
        Sub = in_A - in_M;

        out_B = Sub;
        if (in_M > in_A)
            out_B = Sub + in_q;

    end
    
    // register output
    always @(posedge clk or negedge rstn)
    begin
        if (~rstn)
        begin
            B <= 0;
        end
        else
        begin
            B <= out_B;
        end
    end
    
endmodule
