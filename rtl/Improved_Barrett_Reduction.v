`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Muhammad Ogin Hasanuddin
// 
// Create Date: 2024/02/05 13:00:55
// Design Name: 
// Module Name: barret2
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: Improved_Barrett_Reduction
// # Resource: https://ieeexplore.ieee.org/document/5676912
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module barrett2(
        input clk,
        input rstn,
        input [95:0] X, // assumption X is a result of integer multiplication
        input [47:0] q,
        input [52:0] mu,
        output reg [48:0] r
    );
    
    reg [48:0] q1, q3, r1;  // use reg for always statement
    reg [99:0] q2;
    
    reg [95:0] in_X;
    reg [47:0] in_q;
    reg [52:0] in_mu;
    reg [48:0] out_r;
    
    // register input
    always @(posedge clk, negedge rstn)
    begin
        if (~rstn)
        begin
            in_X <= 0;
            in_q <= 0;
        end
        else
        begin
            in_X <= X;
            in_q <= q;
        end
    end
    
    // reduction
    always @(*)
    begin
        q1 = X >> (48 - 2);
        q2 = q1 * mu;      // need high bit size
        q3 = q2 >> (48 + 5);
        r1 = X - (q3 * q);
    end
    

    // Check for overflow
    always @(*)
    begin
        if (r1 >= q)
            r1 = r1 - q;
        out_r = r1;
    end
    
    // register output
    always @(posedge clk, negedge rstn)
    begin
        if (~rstn)
        begin
            r <= out_r;
        end
        else
        begin
            r <= 0;
        end
    end
        
endmodule
